import pandas as pd
def main():
    
    df = pd.DataFrame()
    df['x'] = [1, 2, 3]
    df['y'] = [1, 2, 3]
    
    df.to_csv('/app/data/data.csv')
    
    print('Hello World')

if __name__ == "__main__":
    main()
