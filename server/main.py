from gabriel_server import cognitive_engine
from gabriel_protocol import gabriel_pb2
from gabriel_server import local_engine
import numpy as np
import cv2


SOURCE = 'roundtrip'


class SandwichEngine(cognitive_engine.Engine):
    def handle(self, input_frame):
        if input_frame.payload_type != gabriel_pb2.PayloadType.IMAGE:
            status = gabriel_pb2.ResultWrapper.Status.WRONG_INPUT_FORMAT
            return cognitive_engine.create_result_wrapper(status)

        np_data = np.fromstring(input_frame.payloads[0], dtype=np.uint8)
        img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
        img = np.rot90(img, 3)

        cv2.imwrite('output.jpg', img)

        raise Exception


def main():
    def engine_factory():
        return SandwichEngine()

    local_engine.run(engine_factory, SOURCE, 60, 9099, 2)


if __name__ == '__main__':
    main()
