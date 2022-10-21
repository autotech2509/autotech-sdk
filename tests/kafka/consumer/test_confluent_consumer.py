from autotech_sdk.kafka.consumer.confluent_consumer import ConfluentConsumer

if __name__ == '__main__':
    from dataclasses import dataclass

    @dataclass
    class GetInforMessage:
        name: str
        age: int

    class GetInforConsumer(ConfluentConsumer):
        class Meta:
            message_type = GetInforMessage

        def process_error_data(self, error):
            pass

        def process_data(self, data):
            name = data.name
            print(name)
