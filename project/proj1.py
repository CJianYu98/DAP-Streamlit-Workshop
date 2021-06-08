import streamlit as st
import pandas as pd
import yfinance as yf

def app():
    # Adding a title for your app page
    st.title('S&P 500 Price Watch App')

    # Add some description for your app/project
    st.markdown("""
    This app shows the **company list** for S&P 500 and their **stock price**!
    * **Python Libraries:** [Streamlit](https://docs.streamlit.io/en/stable/index.html), [Pandas](https://pandas.pydata.org/docs/), [Yahoo Finance](https://pypi.org/project/yfinance/)
    """)

    # Getting the list of S&P 500 companies
    @st.cache
    def get_sp500_companies():
        url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
        html = pd.read_html(url, header = 0)
        df = html[0]
        return df

    sp500_df = get_sp500_companies()
    sp500_symbol = list(sp500_df['Symbol'])
    sectors = sp500_df.groupby('GICS Sector')

    # Add a subheader
    st.header("View Companies by Sectors")

    # Sector selection (multiselect)
    sectors_sorted = sorted(sp500_df['GICS Sector'].unique())
    sectors_selected = st.multiselect('Choose sectors of interest:', sectors_sorted)

    # Filtering data for display
    df_selected_sectors = sp500_df[sp500_df['GICS Sector'].isin(sectors_selected)]

    # Display companies under select sectors
    if sectors_selected:
        st.header("Displaying Companies Under Selected Sectors")
        st.write('Data Dimension: ' + str(df_selected_sectors.shape[0]) + ' rows and ' + str(df_selected_sectors.shape[1]) + ' columns.')
        st.dataframe(df_selected_sectors)

    # Add text input to key in company of interest
    st.header("View Company Stock Price Plots")
    symbol = st.text_input("Enter a company symbol")

    if symbol in sp500_symbol:
        # Getting the data for the company 
        symbol = symbol.upper()
        company_data = yf.Ticker(symbol) 

        # Create options for users to input start & end date, and period options
        start, end, period = st.beta_columns(3)
        start_date = start.date_input('Enter a start date:')
        end_date = end.date_input('Enter an end date:')
        period.selectbox("Choose interval period:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])

        # Get the range of data given the options by user
        company_df = company_data.history(period=period, start=start_date, end=end_date)

        # Add dropdown for user to select type of plots
        plots = st.multiselect('Choose plot:', ['Open', 'Close', 'High', 'Low', 'Volume'])
        plot_title = {
            'Open': 'Opening Price',
            'Close': 'Closing Price',
            'High': 'Highest Price',
            'Low': 'Lowest Price',
            'Volume': 'Trade Volume'
        }

        # Plot all the charts selected
        for plot in plots:
            st.write(f'### {plot_title[plot]}')
            st.line_chart(company_df[plot], use_container_width=True)
    elif symbol == '':
        pass
    else:
        st.error("The company symbol entered does not exists!")




