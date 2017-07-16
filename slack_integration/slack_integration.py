import re
import tensorflow as tf
import execute
from slackbot.bot import respond_to
from slackbot.bot import listen_to

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

@respond_to('.*')
def tf_reply(message):
    message.reply(execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, str(message.body['text'])))
    message.reply("test reply. You said %s" % message.body['text'])
