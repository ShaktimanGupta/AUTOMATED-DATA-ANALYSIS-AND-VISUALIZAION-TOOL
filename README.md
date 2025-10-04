📊 Automated Data Analytics and Visualization Tool

🚀 Project Overview

This repository contains two intelligent data analysis tools designed to automatically analyze datasets and visualize insights with minimal manual effort.

main1 (Static Schema Project) – Works with datasets that have a fixed set of columns.

main2 (Dynamic Schema Project) – Works with datasets that have different or unknown column names, mapping them dynamically during runtime.

Both tools take a CSV file as input, analyze it automatically, and generate meaningful visualizations such as bar charts, pie charts, and trend lines. These projects are built to simplify the data analysis process, making it accessible to both technical and non-technical users.

🧠 Features
main1 (Static Schema Project)

Accepts CSV files that always follow the same column structure.

Automatically performs data cleaning, analysis, and visualization.

Generates summary statistics like average price, total quantity, and region-wise performance.

Creates visualizations such as bar charts, pie charts, and trend graphs.

Best for repetitive analysis where the dataset format never changes.

main2 (Dynamic Schema Project)

Works with datasets that have different column names or structures.

Automatically detects and maps columns dynamically (for example, if one dataset has “Product Name” instead of “Product”, it can identify and use it).

Automatically identifies numeric and categorical data.

Generates charts based on detected columns without requiring any manual modification in the code.

Ideal for general-purpose data analysis when datasets come from multiple sources.

🧰 Technologies Used

Python – Core programming language
Pandas – Data cleaning and analysis
NumPy – Numerical computation
Matplotlib and Seaborn (or Plotly) – Data visualization
Streamlit (optional) – For interactive deployment
CSV / Excel – Input file formats

🗂️ Project Structure

Automated-Data-Analytics-and-Visualization-Tool
│
├── main1 → Static schema project (works with same column names)
├── main2 → Dynamic schema project (handles varying column names)
├── sample_datasets → Example CSV files for testing
└── README.md → Project documentation

⚙️ How to Run the Projects
Running main1 (Static Schema Project)

Open the project folder and ensure Python and required libraries are installed.

Prepare your CSV file with the same columns as the default dataset (for example: Product, Category, Region, Price, Quantity, Month).

Run the file named main1.

The program will read the dataset, clean the data, and automatically generate different visualizations such as bar charts, pie charts, and sales summaries.

Running main2 (Dynamic Schema Project)

Open the project folder and ensure Python and required libraries are installed.

Upload any CSV file (the column names can be different).

Run the file named main2.

The program will detect the columns automatically and generate visualizations based on the mapped schema.

It dynamically adjusts to any dataset, even if column names are different.

🧩 How the Projects Work
For main1 (Static Schema)

The static version expects the same schema every time. When you upload a dataset, it reads the columns like Product, Category, Region, Price, Quantity, and Month. It then calculates total sales, average values, and category-wise performance. After that, it generates visualizations such as bar and pie charts to display insights.

For main2 (Dynamic Schema)

The dynamic version is more advanced. It analyzes the uploaded dataset and automatically identifies equivalent columns (for example, if a file contains “Item Name” instead of “Product” or “Amount” instead of “Price”, it maps them automatically). After mapping, it processes the data and creates graphs showing trends, sales distribution, and comparisons. This makes it ideal for analyzing datasets that don’t follow a fixed format.

📈 Visualizations Generated

• Bar Chart – Product-wise or Category-wise comparison
• Pie Chart – Region or category distribution
• Line Graph – Monthly or time-based sales trend
• Summary Chart – Overall sales analysis and statistics

💡 Use Cases

• Automated data analysis for business reports
• Quick visualization of sales or product performance
• Flexible analytics for different datasets from multiple sources
• Learning and academic projects related to data analytics

🌍 Deployment Options

You can deploy the projects easily on:
• Streamlit Cloud – Free and beginner-friendly hosting for interactive dashboards.
• Render or Railway – To host Python web apps with minimal setup.
• Local System – Run directly using Python IDEs such as VS Code or Jupyter Notebook.

Once deployed, users can upload their own datasets and view results in real time.

👨‍💻 Author

Shaktiman Gupta
B.Tech Computer Science (AI) | Data Analyst | Python Enthusiast
GitHub: https://github.com/ShaktimanGupta

🪪 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with proper credit.

⭐ Contribution

If you find this project useful, please give it a star ⭐ on GitHub!
You can also contribute by improving visualizations, adding new analysis features, or optimizing the column mapping logic.
