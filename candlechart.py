import yfinance as yf
import plotly.graph_objects as go

# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# init_notebook_mode(connected=True) 

# Step 1: Fetch Crypto Data (Bitcoin or Ethereum)
crypto_data = yf.download('BTC-USD', start='2024-01-01', end='2024-06-01')
print(crypto_data.head())  # Check the first few rows of data
crypto_data = crypto_data.dropna()  # Remove rows with missing values

# Step 2: Create the Candlestick Chart
fig = go.Figure(data=[go.Candlestick(
    x=crypto_data.index,
    open=crypto_data['Open'],
    high=crypto_data['High'],
    low=crypto_data['Low'],
    close=crypto_data['Close'],
)])

# Step 3: Customize the Layout (Adding Titles and Labels)
fig.update_layout(
    title='Bitcoin Candlestick Chart',
    yaxis_title='Price in USD',
    xaxis_rangeslider_visible=False,  # Disabling the range slider
    plot_bgcolor='rgb(0, 130, 22)',  # Greenish background color
    font=dict(family='Courier New, monospace', size=15, color='black'),  # Font customization
)

# Step 4: Applying Plotly's Template for a Dark Theme (optional)
fig.update_layout(template='plotly_dark')  # Apply dark theme

# Step 5: Display the Chart
fig.show()


# If you want to switch to Ethereum, simply change the ticker symbol to 'ETH-USD'
# For Ethereum data: yf.download('ETH-USD', start='2023-01-01', end='2023-06-01')
