import argparse
from research.utils.trainer import Config, train

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", "-c", type=str, default=None)
    parser.add_argument("--path", "-p", type=str, default="data")
    parser.add_argument("--device", "-d", type=str, default="auto")
    parser.add_argument("--loss", type=str, default=None)
    parser.add_argument("--beta", type=float, default=None)
    parser.add_argument("--taylor_dim", type=int, default=4)
    parser.add_argument("--env", type=str, default=None)
    args = parser.parse_args()

    config = Config.load(args.config)
    
    config['parse'] = {}
    config['parse']['loss'] = args.loss
    config['parse']['beta'] = args.beta
    config['parse']['taylor_dim'] = args.taylor_dim
    config['parse']['env'] = args.env


    train(config, args.path, device=args.device)