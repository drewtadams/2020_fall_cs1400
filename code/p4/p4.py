

def load_stock_table(stock_file):
    ''' return a stock table (dictionary) with min/max data '''
    try:
        with open(stock_file, 'r') as f:
            # skip over the header
            f.readline()

            #  loop through each row in the csv to get individual stock info
            stocks = {}
            for row in f:
                # break apart the row into individual parts and convert price to float
                record = row.strip().split(',')
                record[2] = float(record[2])
                name = record[0]

                # update the stock
                stock_name = stocks[name] if name in stocks else None
                stocks[name] = update_stock(record, stock_name)

            return stocks

    except FileNotFoundError:
        print(f'file {stock_file} does not exist.')
        return None


def output_stock_data(stocks, file_name='stock_summary.txt'):
    ''' output the stock data to user '''
    # clear the file if it already exists
    open(file_name, 'w').close()

    # loop through each stock and print max, min, and avg and get high/low stocks
    high_low = []
    for name,data in stocks.items():
        out_str = name + '\n' + \
                  '----\n' + \
                  f'Max: {data["max_price"]} {data["max_day"]}\n' + \
                  f'Min: {data["min_price"]} {data["min_day"]}\n' + \
                  f'Ave: {data["total_price"] / data["count"]}\n'
        output(out_str, file_name)

        # update high low
        high_low = update_high_low(high_low, name, data)

    # output high/low stock data
    out_str = f'Highest: {high_low[0][0]} {high_low[0][2]} {high_low[0][1]}\n' + \
              f'Lowest: {high_low[1][0]} {high_low[1][2]} {high_low[1][1]}'
    output(out_str, file_name)


def update_high_low(high_low, stock_name, stock_data):
    ''' return a list containing high and low stocks '''
    # high/low : [ name, day, price ]
    high = [stock_name, stock_data['max_day'], stock_data['max_price']]
    low = [stock_name, stock_data['min_day'], stock_data['min_price']]
    price_i = 2

    # check for default or update
    if len(high_low) == 0:
        high_low = [high]+[low]
    else:
        # update high
        if stock_data['max_price'] > high[price_i]:
            high_low[0] = high

        # update low
        if stock_data['min_price'] < low[price_i]:
            high_low[1] = low

    return high_low


def update_stock(new_record, stock=None):
    ''' create a new stock if stock is None, otherwise update min/max data '''
    # summary_data = {
    #     'AAPL': { 'min_price': 0, 'min_date': '', 'max_price': 0, 'max_date': '' }
    #     'IBM':  { 'min_price': 0, 'min_date': '', 'max_price': 0, 'max_date': '' }
    #     'MSFT': { 'min_price': 0, 'min_date': '', 'max_price': 0, 'max_date': '' }
    # }
    new_day = new_record[1]
    new_price = new_record[2]

    # check if stock exists or not (set defaults or update)
    if stock == None:
        stock = {
            'min_price': new_price,
            'min_day': new_day,
            'max_price': new_price,
            'max_day': new_day,
            'total_price': new_price,
            'count': 1
        }
    else:
        # update max record
        if new_price > stock['max_price']:
            stock['max_price'] = new_price
            stock['max_day'] = new_day

        # update min record
        if new_price < stock['min_price']:
            stock['min_price'] = new_price
            stock['min_day'] = new_day

        # update the total price and count
        stock['total_price'] += new_price
        stock['count'] += 1

    # return the new/updated stock
    return stock


def output(msg, file_name, mode='a'):
    ''' print msg and write it to the passed file_name '''
    print(msg)
    with open(file_name, mode) as f:
        f.write(msg + '\n')


def main():
    stock_file = 'stocks_data.csv'
    stocks = load_stock_table(stock_file)

    if stocks != None:
        output_stock_data(stocks)


if __name__ == '__main__':
    main()