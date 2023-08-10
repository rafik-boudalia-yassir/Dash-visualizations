# Step 0: Make sure to install the necessary libraries
# !pip install dash textblob vaderSentiment

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Step 2: Set up the Dash application
app = dash.Dash(__name__)

# Step 3: Create the layout of the application
app.layout = html.Div([
    html.H1("Sentiment Analysis with TextBlob and VADER"),
    html.Div([
        dcc.Textarea(
            id='text-input',
            value='Enter your text here...',
            style={'width': '100%', 'height': 200},
        ),
        html.Button('Analyze', id='analyze-button', n_clicks=0),
    ]),
    html.Div(id='output-textblob', style={'margin-top': '20px'}),
    html.Div(id='output-vader', style={'margin-top': '20px'}),
])

# Step 4: Define the callback to handle sentiment analysis
analyzer = SentimentIntensityAnalyzer()

@app.callback(
    [Output('output-textblob', 'children'),
     Output('output-vader', 'children')],
    [Input('analyze-button', 'n_clicks')],
    [dash.dependencies.State('text-input', 'value')]
)
def analyze_sentiment(n_clicks, text):
    if not n_clicks:
        return '', ''
    
    # TextBlob Analysis
    tb = TextBlob(text)
    tb_sentiment = tb.sentiment.polarity
    if tb_sentiment > 0:
        tb_result = "Positive"
    elif tb_sentiment < 0:
        tb_result = "Negative"
    else:
        tb_result = "Neutral"
    
    # VADER Analysis
    vs = analyzer.polarity_scores(text)
    if vs['compound'] >= 0.05:
        vader_result = "Positive"
    elif vs['compound'] <= -0.05:
        vader_result = "Negative"
    else:
        vader_result = "Neutral"
    
    return f'TextBlob Sentiment: {tb_result}', f'VADER Sentiment: {vader_result}'

# Step 5: Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
