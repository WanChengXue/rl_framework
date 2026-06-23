import pickle
import zmq
from rl_framework.utils.config import ParseConfig


class BaseServer:
    def __init__(self, config_path: str):
        config_dict = ParseConfig(config_path)()
        self.config_dict = config_dict
        self.context = zmq.Context()
        self.context.setsockopt(zmq.MAX_SOCKETS, 10000)
        self.poller = zmq.Poller()
        self.log_sender = self.context.socket(zmq.PUSH)
        self.log_sender.connect(
            f"tcp://{self.config_dict['log_server_address']}:{self.config_dict['log_server_port']}"
        )
        self.cached_log_list = []

    def send_log(self, log_dict: dict, send_threshold: int = 10):
        """向日志服务器批量发送日志，默认每十条发送一次。"""
        self.cached_log_list.append(log_dict)
        if len(self.cached_log_list) >= send_threshold:
            payload = pickle.dumps(self.cached_log_list)
            self.log_sender.send(payload)
            self.cached_log_list = []

    def recursive_send(self, log_info, prefix_string: str | None, suffix_string: str | None = None):
        """
        递归展开嵌套结构（dict / list / tuple），拼接 key 路径后发送日志。

        示例:
            {"loss": {"actor": 1.0, "critic": 2.0}}
            => 生成 "loss/actor": 1.0, "loss/critic": 2.0
        """
        if isinstance(log_info, dict):
            for key, value in log_info.items():
                new_prefix = f"{prefix_string}/{key}" if prefix_string else key
                self.recursive_send(value, new_prefix, suffix_string)
        elif isinstance(log_info, (tuple, list)):
            for index, value in enumerate(log_info):
                new_prefix = f"{prefix_string}_{index}" if prefix_string else str(index)
                self.recursive_send(value, new_prefix, suffix_string)
        else:
            key = f"{prefix_string}/{suffix_string}" if suffix_string else prefix_string
            self.send_log({key: log_info})
