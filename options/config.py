# -*- coding: utf-8 -*-
# Copyright 2019 Huairuo.ai.
# Author: Lin Li (li.lin@huairuo.ai)
#
# cython: language_level=3
#

class Config(object):

  def __init__(self):
    # basemode cfg
    self.gpu_ids = []
    self.isTrain = True
    self.checkpoints_dir = "./check_point"
    self.name = "cycle_gan_modify"
    self.preprocess = "" # 如果数据输入维度每次变化较大， 设置为 scale_width
    # local cfg
    self.lambda_identity = 0 # identity weight?
    self.input_nc = 3 # the number of  channel in input file.
    self.output_nc = 3 # the number of channels in output images
    self.ngf = 3 # the number of filters in the last conv layer
    self.netG = "resnet_6blocks" # the architecture's name: resnet_9blocks | resnet_6blocks | unet_256 | unet_128
    self.norm = 'batch' # the name of normalization layers used in the network: batch | instance | none
    self.use_dropout = False # if use dropout layers.
    self.init_type = 'normal' # the name of our initialization method: : normal | xavier | kaiming | orthogonal
    self.init_gain = 0.02 # scaling factor for normal, xavier and orthogonal.
    self.epoch_count = 20000
    self.ndf = 3 # the number of filters in the first conv layer
    self.n_layers_D = 3 # the number of conv layers in the discriminator; effective when netD=='n_layers'
    self.netD = "basic" # the architecture's name: basic | n_layers | pixel
    self.lr_policy = "linear" # the name of learning rate policy: linear | step | plateau | cosine
    self.continue_train = False # is continue train.
    self.load_iter = 0
    self.epoch = 100
    self.niter = 100
    self.niter_decay = 100
    self.batch_size = 2
    self.save_latest_freq = 50 #
    self.save_by_iter = 50 #
    self.save_epoch_freq = 50 #
    # display
    self.verbose = True # (bool) -- if verbose: print the network architecture
    self.display_id = 1 # window id of the web display
    self.no_html = False #
    self.display_winsize = 256 # display window size for both visdom and HTML
    self.display_server = "localhost" #
    self.display_port = 99 #
    self.display_ncols = 5 #
    self.display_env = "main" # visdom display environment name (default is "main")
    self.print_freq = 50 #
    self.display_freq = 50 #
    self.update_html_freq = 50 #
