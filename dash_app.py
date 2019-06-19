import random
import numpy as np
import pandas as pd

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import plotly.graph_objs as go


# DataFrames
df1 = pd.read_csv("C:\\Users\\hp\\Desktop\\Données\\Talents_List_Dash.csv")
pred = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Predictor")
month1 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month1")
month2 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month2")
month3 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month3")
month4 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month4")
month5 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month5")
month6 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month6")
month7 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month7")
month8 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month8")
month9 = pd.read_excel("C:\\Users\\hp\\Desktop\\Données\\base de donnée projet edacy notes arrangées.xlsx",sheet_name="Month9")


# APP
external_stylesheets = [
    # "https://codepen.io/chriddyp/pen/bWLwgP.css",
    dbc.themes.BOOTSTRAP
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div(
    
    # ENTIRE APP LAYOUT
    [
        # Navigation BAr
        dbc.NavbarSimple(
            brand="ANALYTIX",
            brand_href="http://127.0.0.1:8050",
            color="#F5F5F5",
            brand_style={
                "text-align": "center",
                "font-size": "26px",
                "font-weight": "bold",
                "height": "80",
                "marginTop": 20,
                "marginBottom": 20,
            },
            children= dbc.Button(
                "Make Prediction",
                className="mr-1",
                style={
                    "color": "black",
                    "marginBottom": 50,
                    "marginTop": 20,
                    "float": "left",
                    "width": "190px",
                    "backgroundColor": "#FFCC00",
                    "border": "#FFCC00",
                    "marginLeft": 50, "backgroundColor": "#FFCC00",
                },
            ),
        ),
        
        
        html.Div(
            [
                html.Div(
                    dcc.Tabs(
                        parent_style={"font-size": "20px"},
                        id="tabs",
                        value="Talents",
                        children=[
                            dcc.Tab(label="TALENTS", value="Talents"),
                            dcc.Tab(label="INSTRUCTORS", value="Instructors"),
                        ],
                        colors={
                            "border": "white",
                            "primary": "#FFCC00",
                            "background": "#FFFFFF",
                        },
                        style={"margin": "80", "marginTop": 0},
                    )
                ),
                html.Div(id="tabs-content"),
            ]
        ),
        
        # Make Prediction Button
        html.Br(),
        html.Div(
            dbc.Modal(
                "Table",
                className="mr-1",
                style={
                    "color": "black",
                    "marginBottom": 50,
                    "marginTop": 20,
                    "float": "left",
                    "width": "190px",
                    "backgroundColor": "#FFCC00",
                    "border": "#FFCC00",
                },
            ),
        ),
    ]
)
html.Br()


@app.callback(Output("tabs-content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "Talents":
        return (
            html.Div(
                [
                    # Dropdowns
                    html.Div(
                        [
                            dcc.Dropdown(
                                options=[
                                    {"label": "All Cohorts", "value": "Cohortes"},
                                    {"label": "Cohorte 1", "value": "C1"},
                                    {"label": "Cohorte 3", "value": "C2"},
                                    {"label": "Cohorte 4", "value": "C4"},
                                    {"label": "Cohorte 5", "value": "C5"},
                                    {"label": "Cohorte 6", "value": "C6"},
                                    {"label": "Cohorte 7", "value": "C7"},
                                ],
                                value=["Cohortes"],
                                multi=False,
                                style={
                                    "marginLeft": 35,
                                    "marginRight": 0,
                                    "marginTop": 0,
                                    "marginBottom": 0,
                                    "width": "180px",
                                },
                            )
                        ]
                    ),
                    # Talents graph
                    html.Div(
                        [
                            # 1st graph
                            dbc.Row(
                                [
                                    dbc.Col(
                                        html.Div(
                                            dcc.Graph(
                                                id="graph-1-tabs",
                                                figure={
                                                    "data": [
                                                        {
                                                            "x": [""],
                                                            "y": [
                                                                np.mean(pred["Hard_Score"]).round()
                                                            ],
                                                            "type": "bar",
                                                            "name": "Hard Skills",
                                                            # edacy blue
                                                            "marker": {
                                                                "color": "#61BFAD"
                                                            },
                                                        },
                                                        {
                                                            "x": [""],
                                                            "y": [
                                                                np.mean(pred["Soft_Score"]).round()
                                                            ],
                                                            "type": "bar",
                                                            "name": "Soft Skills",
                                                            # edacy yellow
                                                            "marker": {
                                                                "color": "#FFCC00"
                                                            },
                                                        },
                                                    ]
                                                },
                                                style={"width": "100%"},
                                            ),
                                            # style={"order": 1}
                                        )
                                    ),
                                    # 2nd graph
                                    dbc.Col(
                                        html.Div(
                                            dcc.Graph(
                                                id="graph-2-tabs",
                                                figure={
                                                    "data": [
                                                        {
                                                            "x": [""],
                                                            "y": [
                                                                np.mean(
                                                                    df1["Hard_Score"]
                                                                ).round(1)
                                                            ],
                                                            "type": "bar",
                                                            "name": "Skills",
                                                            # edacy blue
                                                            "marker": {
                                                                "color": "#61BFAD"
                                                            },
                                                        },
                                                        {
                                                            "x": [""],
                                                            "y": [
                                                                np.mean(
                                                                    df1["Soft_Score"]
                                                                ).round(1)
                                                            ],
                                                            "type": "bar",
                                                            "name": "Soft",
                                                            # edacy yellow
                                                            "marker": {
                                                                "color": "#FFCC00"
                                                            },
                                                        },
                                                    ]
                                                },
                                                style={"width": "100%"},
                                            )
                                        ),
                                        # style={'backgroundColor':'#F5F5F5'}
                                    ),
                                ]
                            )
                        ]
                    ),
                    # Table title
                    # html.H4(
                    #     "Talents DataTable",
                    #     style={
                    #         "marginLeft": 50,
                    #         "marginRight": 0,
                    #         "marginTop": 0,
                    #         "marginBottom": 0,
                    #         "width": "50%",
                    #     },
                    # Table
                    html.Div(
                        # dash_table.DataTable(
                        #     id="table",
                        #     columns=[{"name": i, "id": i} for i in df1.columns],
                        #     data=df1.to_dict("records"),
                        #     style_table={"overflowX": "scroll"},
                        #     n_fixed_rows=1,
                        #     style_cell={
                        #         "minWidth": "150px",
                        #         "width": "150px",
                        #         "maxWidth": "150px",
                        #     },
                        # ),
                        # style={
                        #     "width": "90%",
                        #     "height": "40%",
                        #     "marginLeft": 50,
                        #     "marginRight": 0,
                        #     "marginTop": 10,
                        #     "marginBottom": 0,
                        # },
                        dbc.Table.from_dataframe(
                            df1,
                            striped=True,
                            bordered=True,
                            hover=True,
                            size="lg",
                            responsive=True,
                        ),
                        style={
                            "width": "90%",
                            "margin-left": "auto",
                            "margin-right": "auto",
                        },
                    ),
                ]
            ),
        )

    elif tab == "Instructors":
        return html.Div(
            [
                html.Div(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        dcc.Graph(
                                            id="graph-tabs_1",
                                            figure={
                                                "data": [
                                                    {
                                                        "x": [1, 2, 3],
                                                        "y": [5, 10, 6],
                                                        "type": "bar",
                                                        "marker": {"color": "#61BFAD"},
                                                    }
                                                ]
                                            },
                                            style={"width": "100%"},
                                        )
                                    )
                                ),
                                dbc.Col(
                                    html.Div(
                                        dcc.Graph(
                                            id="graph-tabs_2",
                                            figure={
                                                "data": [
                                                    {
                                                        "x": [10, 20, 30],
                                                        "y": [5, 10, 6],
                                                        "type": "bar",
                                                        "marker": {"color": "#61BFAD"},
                                                    }
                                                ]
                                            },
                                            style={"width": "100%"},
                                        )
                                    )
                                ),
                            ]
                        )
                    ]
                )
            ]
        )


if __name__ == "__main__":
    app.run_server(debug=True)
