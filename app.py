from flask import Flask, render_template, request, redirect
from PlotStockPrice import get_dates, get_stock_data, plot_stocks
from forms import TickerForm

app = Flask(__name__)
app.config.from_object('config')

#from flask.ext.sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/VickyQian'
#db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
  script = None
  div = None
  show_form = True
  form = TickerForm()
  if form.validate_on_submit():
    ticker = form.ticker_symbol.data
    #flash('You entered: %s' % (company))

    dates = get_dates()

    sdata = get_stock_data(ticker, dates[0], dates[1])
    #if sdata.empty:
    #  bad_result = 'Data for {} not found'.format(company)
    #else:
    values = [form.closing_price.data, form.adj_close.data, form.opening_price.data, form.adj_opening.data]
    print(values)
    script, div = plot_stocks(sdata, ticker, values)
    show_form = False
    
  #script, div = plot_stocks(get_stock_data('AAPL','2017-09-06','2017-10-06'), 'AAPL')
  return render_template('index.html', form = form,script=script, div=div, show_form = show_form)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
  
