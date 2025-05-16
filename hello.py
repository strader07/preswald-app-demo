from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
df = get_df("data/teams.csv")
df["stadium_id"] = df["stadium_id"].astype(int)

sql = "SELECT * FROM data/teams.csv where founded_year > '1930'"
filtered_df = query(sql, "data/teams.csv")

text("# Structured Labs Demo APP")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="stadium_id", y="founded_year")
plotly(fig)
