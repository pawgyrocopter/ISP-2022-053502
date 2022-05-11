
from gyrocopter._serializers.abstractSerializer import AbstractSerializer


class TomlSerializer(AbstractSerializer):
    def dump(self, _object, file_path):
        pass

    def dumps(self, _object):
        pass

    def load(self, file_path):
        pass

    def loads(self, string):
        pass

