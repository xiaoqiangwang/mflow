import numpy


class Handler:

    def receive(self, receiver):

        header = receiver.next(as_json=True)
        return_value = None
        data = []

        # header contains: "htype", "shape", "type", "frame", "endianess", "source", "encoding", "tags"

        # Receiving data
        while receiver.has_more():
            raw_data = receiver.next()
            if raw_data:
                data.append(get_image(raw_data, header['type'], header['shape']))
            else:
                data.append(None)

        if header or data:
            return_value = {'header': header,
                            'data': data}

        return return_value


def get_image(raw_data, dtype, shape):
    return numpy.fromstring(raw_data, dtype=dtype).reshape(shape)
