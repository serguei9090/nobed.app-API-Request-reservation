import pandas as pd

# Create table
def table(booking_info):
    df = pd.DataFrame(booking_info)
    df.index = df.index + 1
    
    # Define a function to apply the styles
    def style_table(df):
        return df.style.set_table_styles(
            [
                {'selector': 'thead th', 'props': [('background-color', '#009879'), ('color', 'white'), ('text-align', 'left'), ('font-weight', 'bold'), ('padding', '0.5rem 0.7rem'), ('border', '1px solid black')]},
                {'selector': 'tbody td', 'props': [('padding', '0.5rem 0.7rem'), ('border', '1px solid black')]},
                {'selector': 'tbody tr:nth-of-type(even)', 'props': [('background-color', '#f3f3f3')]},
                {'selector': 'tbody tr:hover', 'props': [('background-color', '#dddddd')]},
                {'selector': 'tbody tr:last-of-type', 'props': [('border-bottom', '2px solid #009879')]},
                {'selector': 'tbody tr.active-row', 'props': [('font-weight', 'bold'), ('color', '#009879')]},
                {'selector': 'table', 'props': [('border-collapse', 'collapse'), ('margin', '25px 0'), ('font-size', '1rem'), ('min-width', '400px'), ('border-radius', '5px 5px 0 0'), ('overflow', 'hidden'), ('box-shadow', '0 0 20px rgba(0, 0, 0, 0.25)')]}
            ]
        ).set_properties(**{'text-align': 'left'})
    
    # Apply the styles and convert to HTML
    styled_df = style_table(df)
    html_table = styled_df.to_html(escape=False)
    
    # Wrap the table content in HTML and CSS
    html_content = f"""
    <html>
    <head>
        <style type="text/css">
            thead th {{
                background-color: #009879;
                color: white;
                text-align: left;
                font-weight: bold;
                padding: 0.5rem 0.7rem;
                border: 1px solid black;
            }}
            tbody td {{
                padding: 0.5rem 0.7rem;
                border: 1px solid black;
            }}
            tbody tr:nth-of-type(even) {{
                background-color: #f3f3f3;
            }}
            tbody tr:hover {{
                background-color: #dddddd;
            }}
            tbody tr:last-of-type {{
                border-bottom: 2px solid #009879;
            }}
            tbody tr.active-row {{
                font-weight: bold;
                color: #009879;
            }}
            table {{
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1rem;
                min-width: 400px;
                border-radius: 5px 5px 0 0;
                overflow: hidden;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.25);
            }}
        </style>
    </head>
    <body>
        {html_table}
    </body>
    </html>
    """
    
    return html_content
