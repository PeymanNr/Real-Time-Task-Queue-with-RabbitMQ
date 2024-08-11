import unittest
from unittest.mock import MagicMock, patch
import pika
from task_consumer import callback


class TestConsumer(unittest.TestCase):

    @patch('consumer.task_consumer.channel')
    def test_callback(self, mock_channel):
        mock_method = MagicMock()
        mock_properties = MagicMock()
        mock_properties.reply_to = 'reply_queue'
        mock_properties.correlation_id = '12345'

        mock_channel.basic_publish = MagicMock()
        mock_channel.basic_ack = MagicMock()

        body = 'Hello'

        callback(mock_channel, mock_method, mock_properties,
                 body.encode('utf-8'))

        mock_channel.basic_publish.assert_called_once_with(
            exchange='',
            routing_key='reply_queue',
            properties=pika.BasicProperties(correlation_id='12345'),
            body=b'Hello back!'
        )

        mock_channel.basic_ack.assert_called_once_with(
            delivery_tag=mock_method.delivery_tag)


if __name__ == '__main__':
    unittest.main()
