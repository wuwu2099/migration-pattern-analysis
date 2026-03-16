# Migration Patterns in Coeur d' Alene and Spokane Area

**Objective:** Analyze regional migration patterns in Coeur d'Alene (ID) and Spokane (WA) to uncover trends in population movement, with a focus on comparing the two areas for more precise insights.

**Key Skills:** Python, Pandas, GIS, Data Visualization, Spatial Analysis

**Dataset:** Census Demographic and Spatial Data 

---

A data analysis project exploring migration patterns in the Coeur d'Alene (Idaho) and Spokane (Washington) metropolitan areas. The project compares the two regions to better understand local population movement and regional dynamics.

This project uses Python-based data analysis and geographic data visualization to examine migration trends. The goal is to demonstrate data cleaning, exploratory analysis, and spatial visualization skills in a real regional case study.


## Problem

The Coeur d'Alene (Idaho) region has experienced rapid population growth in recent years. Many new residents are relocating to the area due to factors such as natural amenities, recreational opportunities, and a lower cost of living compared to larger metropolitan regions. Coeur d'Alene is also closely connected with nearby cities in the Spokane (Washington) area. Residents frequently move between or interact across these regions for employment, recreation, and services, forming a small but dynamic regional system.

Rapid migration into the region can create significant impacts on housing demand, childcare availability, healthcare services, and other infrastructure needs. Understanding migration patterns is therefore important for interpreting how population changes shape local communities.

This project conducts a data-driven analysis of migration patterns in the Coeur d'Alene and Spokane areas to better understand where migrants come from, who they are demographically, and what factors may be influencing these population movements.

---

## Research Question

What migration patterns are shaping population growth in the Coeur d'Alene and Spokane areas in terms of where migrants come from (within-state vs. out-of-state), who they are demographically, and what factors may be driving these relocation decisions?

---

## Analysis Goals

- Examine migration inflows into the Coeur d'Alene and Spokane areas by distinguishing **within-state and out-of-state migration patterns**.
- Analyze the **demographic characteristics of incoming migrants** using Census population data.
- Explore **potential drivers of migration**, such as housing conditions, employment opportunities, and regional amenities.
- Compare migration dynamics between the **Coeur d'Alene and Spokane areas** to identify similarities and differences in regional population change.

## Data

This project uses publicly available demographic and migration data from the U.S. Census Bureau. The analysis is conducted at the **census tract** level, a geographic unit designed by the Census Bureau to represent relatively stable neighborhood-sized populations for statistical analysis.

The dataset contains **169 census tracts** covering the Coeur d'Alene (Idaho) and Spokane (Washington) regions, with **variables** describing spatial migration patterns and demographic characteristics.

Note: Raw datasets are not stored in this repository due to file size.
They can be downloaded from the original public data source.

## Tools and Technologies

- **Python** – data processing and analysis
- **Pandas** – data manipulation and transformation
- **Matplotlib** – data visualization
- **GWR** – spatial analysis of migration patterns
- **ArcGIS** – spatial regression analysis and map making


## Project Structure

migration-analysis-coeurdalene-spokane/

├── data/  
│   ├── raw/          # Original datasets  
│   └── processed/    # Cleaned and prepared datasets  

├── src/              # Python scripts for data processing and analysis  

├── results/          # Analysis outputs: tables, maps, and images  

└── README.md         # Project overview and instructions