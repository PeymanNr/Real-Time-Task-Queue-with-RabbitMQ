import unittest
from unittest.mock import patch, Mock
from task_producer import callback


class TestProducer(unittest.TestCase):

    @patch('producer.task_producer.rabbit_connection')
    def test_producer_send_message(self, mock_connection):
        mock_channel = Mock()
        mock_uuid = '123'
        mock_message = 'Hello'

        callback(mock_channel, None, None, mock_message)

        mock_channel.queue_declare.assert_called_once_with(queue=mock_uuid)
        mock_channel.basic_publish.assert_called_once()


if __name__ == '__main__':
    unittest.main()

