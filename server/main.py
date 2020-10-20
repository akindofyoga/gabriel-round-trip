#!/usr/bin/env python3

from gabriel_server import cognitive_engine
from gabriel_protocol import gabriel_pb2
from gabriel_server import local_engine
import logging


SOURCE = 'roundtrip'


logging.basicConfig(level=logging.INFO)


class RoundTripEngine(cognitive_engine.Engine):
    def handle(self, input_frame):
        if input_frame.payload_type != gabriel_pb2.PayloadType.IMAGE:
            status = gabriel_pb2.ResultWrapper.Status.WRONG_INPUT_FORMAT
            return cognitive_engine.create_result_wrapper(status)

        result = gabriel_pb2.ResultWrapper.Result()
        result.payload_type = gabriel_pb2.PayloadType.IMAGE
        result.payload = input_frame.payloads[0]

        status = gabriel_pb2.ResultWrapper.Status.SUCCESS
        result_wrapper = cognitive_engine.create_result_wrapper(status)
        result_wrapper.results.append(result)

        return result_wrapper


def main():
    def engine_factory():
        return RoundTripEngine()

    local_engine.run(engine_factory, SOURCE, 60, 9099, 2)


if __name__ == '__main__':
    main()
