import polars as pl

catalog: pl.DataFrame = pl.read_csv(
    source="space_apps_2024_seismic_detection/data/lunar/training/catalogs/apollo12_catalog_GradeA_final.csv"
)
json_file: pl.DataFrame = pl.DataFrame(
    schema={
        "filename": pl.String(),
        "time_rel": pl.Float64(),
    }
)

for i in range(len(catalog)):
    json_file = json_file.extend(
        other=pl.DataFrame(
            data={
                "filename": [catalog["filename"][i]],
                "time_rel": [catalog["time_rel(sec)"][i]],
            }
        )
    )

json_file.write_json(file="train.json")
json_file.write_csv(file="train.csv")
