import pandas as pd
import numpy as np
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px

# 1. Generate Sample Student Data
np.random.seed(42)  # For reproducibility
num_students = 100
data = {
    'StudentID': range(1, num_students + 1),
    'MathScore': np.random.randint(60, 100, num_students),
    'ScienceScore': np.random.randint(50, 95, num_students),
    'EnglishScore': np.random.randint(70, 100, num_students),
    'Attendance': np.random.uniform(0.8, 1.0, num_students),
    'AssignmentsCompleted': np.random.randint(5, 10, num_students),
    'StudyHours': np.random.uniform(10, 30, num_students),
    'Extracurriculars': np.random.choice(['Yes', 'No'], num_students)
}
df = pd.DataFrame(data)
df['AverageScore'] = df[['MathScore', 'ScienceScore', 'EnglishScore']].mean(axis=1)

# 2. Create Dash App
app = dash.Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f9f9f9'}, children=[
    html.Div(
        html.H1("Student Performance Dashboard", style={'color': 'white', 'textAlign': 'center', 'padding': '20px'}),
        style={'backgroundColor': '#4682B4'}  # Steel Blue
    ),

    html.Div(style={'display': 'grid', 'gridTemplateColumns': 'repeat(3, 1fr)', 'gap': '20px', 'padding': '20px'}, children=[
        # Academic Performance
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Academic Performance"),
            dcc.Graph(figure=px.histogram(df, x='AverageScore', title='Average Score Distribution'))
        ]),

        # Subject Performance
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Subject Performance"),
            dcc.Graph(figure=px.bar(df.melt(value_vars=['MathScore', 'ScienceScore', 'EnglishScore'], var_name='Subject', value_name='Score'), x='Subject', y='Score', color='Subject', barmode='group', title = "Subject Scores"))
        ]),

        # Attendance
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Attendance"),
            dcc.Graph(figure=px.scatter(df, x='StudentID', y='Attendance', title='Attendance Rate'))
        ]),

        # Assignments/Projects
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Assignments/Projects"),
            dcc.Graph(figure=px.histogram(df, x='AssignmentsCompleted', title='Assignments Completed'))
        ]),

        # Study Time
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Study Time"),
            dcc.Graph(figure=px.box(df, y='StudyHours', title='Study Hours Distribution'))
        ]),

        # Extracurricular Activities
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Extracurricular Activities"),
            dcc.Graph(figure=px.histogram(df, x='Extracurriculars', title = "Extracurricular Participation"))
        ]),

        # Progress Overview
        html.Div(style={'border': '1px solid #ddd', 'padding': '15px'}, children=[
            html.H3("Progress Overview"),
            dcc.Graph(figure=px.line(df.sort_values('AverageScore'), x='StudentID', y='AverageScore', title='Student Progress'))
        ]),
    ])
])

# 3. Run the App
if __name__ == '__main__':
    app.run_server(debug=True)