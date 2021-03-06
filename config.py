
def get_default_config(dataset):
    if dataset=='imagenet':
       batch_size = 32
       image_size = 224
       lr = 1e-3
       c = 1000
       epoch = 100
       is_sgd = False
    elif dataset == 'imagewoof':
       batch_size = 32
       image_size = 224
       lr = 1e-3
       c = 10
       epoch = 100
       is_sgd = False
    elif dataset == 'cifar100':
       batch_size = 64
       image_size = 32
       lr = 1e-3
       c = 100
       epoch = 150
       is_sgd = False
    elif dataset == 'cifar10':
       batch_size = 64
       image_size = 32
       lr = 1e-3
       c = 10
       epoch = 100
       is_sgd = False
    elif dataset == 'pets':
       batch_size = 64
       image_size = 224
       lr = 1e-3
       c = 37
       epoch = 100
       is_sgd = False
    return batch_size,image_size,lr,c,epoch,is_sgd
