import argparse

def main():
    parser = argparse.ArgumentParser(description="딥러닝 학습 스크립트")
    parser.add_argument("--epochs", type=int, default=10, help="학습 에포크 수")
    parser.add_argument("--batch_size", type=int, default=32, help="배치 크기")
    args = parser.parse_args()
    print(f"에포크:{args.epochs}, 배치 크기:{args.batch_size}")

if __name__ == "__main__":
    main()
    