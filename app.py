from flask import Flask, request, render_template_string
from scraping_functions import scraper
from styler import color_background

"""
keyword search: steam wand
longer query: espresso machine steam wand with automatic temperature sensing and adjustable temperature and froth levels
"""
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    query = ''
    holistic_query = ''
    df_html = ''
    if request.method == 'POST':
        query = request.form.get('query', '')  # Capture the first query
        holistic_query = request.form.get('holistic_query', '')  # Capture the second query
        df = scraper(query, holistic_query)

        # Format the 'Link' column to be clickable
        df['Link'] = df['Link'].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')

        # Apply the style
        styled_df = df.style.map(color_background, subset=['Cosine Similarity'])

        # Convert the styled DataFrame to HTML
        df_html = styled_df.to_html(escape=False, index=False)

    return render_template_string(HTML_TEMPLATE, index=False, query=query, holistic_query=holistic_query,
                                  tables=[df_html] if df_html else None)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Patent Search Interface</title>
        <style>
            h1, h2 {
                text-align: center;
                font-size: 2em; /* Increase font size by 4 units (assuming 1em = 16px, this is 32px) */
            }
            .dataframe th {
                text-align: center;
                font-size: 1.25em; /* Increase font size by 4 units (assuming 1em = 16px, this is 20px) */
            }
            .dataframe th, .dataframe td {
                border: 1px solid #ddd;
                padding: 8px;
                white-space: normal; /* Allow text wrapping */
                word-wrap: break-word; /* Break long words */
            }
            .dataframe th {
                background-color: #f2f2f2;
                text-align: center;
                }
            footer {
                text-align: center;
                font-size: 0.8em; /* Smaller font size */
                color: grey; /* Grey color */
                margin-top: 20px; /* Space above the footer */
            }
            .query-container {
                display: flex;
                justify-content: center;
                gap: 20px;
            }
            textarea {
                width: 200px;
                height: 100px;
            }
            .button-container {
                text-align: center;
                margin-top: 10px;
            }
            .dataframe {
                table-layout: auto; /* Auto layout for responsive column width */
                max-width: 100%; /* Maximum width of the table */
                width: auto; /* Automatic width */
                margin: auto; /* Center the table */
                border-collapse: collapse; /* Collapsed borders */
        }
        </style>
        <script>
            function validateForm() {
                var query = document.getElementById('query').value.trim();
                var holisticQuery = document.getElementById('holistic_query').value.trim();
                if (query === '' || holisticQuery === '') {
                    alert('Both query fields must be filled out.');
                    return false;
                }
                return true;
            }
        </script>
    </head>
    <body>
        <h1>Patent Search Interface</h1>
        <form method="post" onsubmit="return validateForm();">
            <div class="query-container">
                <div>
                    <label for="query">Keyword Search:</label><br>
                    <textarea id="query" name="query">{{ query }}</textarea>
                </div>
                <div>
                    <label for="holistic_query">Longer Holistic Query:</label><br>
                    <textarea id="holistic_query" name="holistic_query">{{ holistic_query }}</textarea>
                </div>
            </div>
            <div class="button-container">
                <input type="submit" value="Search">
            </div>
       </form>
    {% if tables %}
      <h2>Results</h2>
      {% for table in tables %}
        {{ table|safe }}
      {% endfor %}
    {% endif %}
    <footer>
        Caleb Estes, Alan Crisologo, Corey Luksch, Alexandra Batko
    </footer>
  </body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)