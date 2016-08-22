#from __future__ import print_function

from oslo_config import cfg

simple_group = cfg.OptGroup(name='simple',
                         title='A Simple Example')


naive_group = cfg.OptGroup(name='naive',
                         title='A Naive Example')


simple_opts = [cfg.BoolOpt('enable',default=False,help=('True enables, False disables'))]

naive_opts = [cfg.StrOpt('message',default="Hello World",help=('Say Hello World'))]

CONF = cfg.CONF 

CONF.register_group(simple_group)

CONF.register_opts(simple_opts,simple_group)

CONF.register_group(naive_group)

CONF.register_opts(naive_opts,naive_group)


if __name__ =="__main__":

    CONF(default_config_files=['app.conf'])

    print('[simple] enable:{}'.format(CONF.simple.enable))

    print('[naive] message:{}'.format(CONF.naive.message))
