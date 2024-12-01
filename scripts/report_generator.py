
import pandas as pd

df = pd.read_excel("../notebooks/Final_Influencer_Data_insights_up_dec1_t2.xlsx")
html_content = """
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        table {
            width: 95%;
            border-collapse: collapse;
            margin: 20px auto;
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: center;
            padding: 20px;
            font-size: 16px;
        }
        th {
            background-color: #f2f2f2;
            font-size: 18px;
        }
        img {
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
    </style>
</head>
<body>
    <h1 style="text-align:center;">Influencer Performance Report</h1>
    <table>
        <tr>
            <th>Influencer Label</th>
            <th>Influencer Pic</th>
            <th>Average Performance</th>
            <th>Video URL</th>
        </tr>
"""

for index, row in df.iterrows():
    img_url = row.get('Influencer Pic URL', '')
    if isinstance(img_url, str):
        img_url = img_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    else:
        img_url = ""

    influencer_label = str(row.get('Influencer Label', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    average_performance = str(row.get('Average Performance', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    video_url = str(row.get('Video URL', '')).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    html_content += f"""
        <tr>
            <td>{influencer_label}</td>
            <td><img src="{img_url}" alt="Image Not Found"></td>
            <td>{average_performance}</td>
            <td><a href="{video_url}" target="_blank">Video Link</a></td>
        </tr>
    """

html_content += """
    </table>
</body>
</html>
"""

with open("../output/influencer_report_up.html", "w") as f:
    f.write(html_content)

print("HTML report saved.")
