import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the data
df = pd.read_csv('cleaned_sales_data.csv')

# Check the data structure
print("Data shape:", df.shape)
print("Columns:", df.columns.tolist())
print("First few rows:")
print(df.head())

# Count each product type
product_counts = df['product'].value_counts().reset_index()
product_counts.columns = ['product', 'count']
print("\nProduct counts:")
print(product_counts)

# Create bar chart showing product distribution
fig = px.bar(product_counts, 
             x='product', 
             y='count',
             title='Product Dist',  # Keep under 40 chars and under 15 chars actually
             color='product',
             color_discrete_sequence=['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', 
                                    '#B4413C', '#964325', '#944454', '#13343B'])

# Update layout and styling - remove cliponaxis as it doesn't exist for axes
fig.update_xaxes(title='Product')  # Keep under 15 chars
fig.update_yaxes(title='Count')    # Keep under 15 chars

# Remove legend since x-axis already shows product names and colors
fig.update_layout(showlegend=False)

# Save the chart
fig.write_image('product_distribution.png')
fig.show()