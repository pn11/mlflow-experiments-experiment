import argparse

import mlflow

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('num_experiments', type=int)
    parser.add_argument('--use_sqlite', action='store_true')

    if args is None:
        return parser.parse_args()
    else:
        return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = parse_args()

        if args.use_sqlite:
            mlflow.set_tracking_uri("sqlite:///./mlruns.sqlite3")
        
        for i in range(args.num_experiments):
            mlflow.set_experiment(f"experiment{i}")
            mlflow.start_run(run_name=f"run{i}")
            mlflow.log_params(args.__dict__)
            mlflow.log_metrics({"id":i})
            mlflow.end_run()

if __name__ == '__main__':
    main()



