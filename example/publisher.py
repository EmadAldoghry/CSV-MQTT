from csv_mqtt import CsvMqtt

Path_csv = "./example/sample.csv"
connector = CsvMqtt("broker.hivemq.com")
connector.publish_csv_data(Path_csv, "Topic_example")