import dbconnection
import pandas as pd
import neo4j
import plotdata



class main:
    ''''Main app class for data visualization'''

    def main():
        d = dbconnection.dbconnection("config.yaml")
        # dbconnection
        connection = d.get_neo_connection()
        connection.execute_query("MATCH (n) DETACH DELETE n")
        # Loads CSV into Neo4j
        connection.execute_query("LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/EvanTy11/FinalProject/master/Electric_Vehicle_Population_Data.csv' AS line WITH collect(line) AS rows UNWIND rows AS row CREATE (:VehicleRegistration {     VIN: row.`VIN (1-10)`,     County: row.`County`,     City: row.`City`,     State: row.`State`,     PostalCode: row.`Postal Code`,     ModelYear: row.`Model Year`,     Make: row.`Make`,     Model: row.`Model`,     ElectricVehicleType: row.`Electric Vehicle Type`,     CAFVEligibility: row.`Clean Alternative Fuel Vehicle (CAFV) Eligibility`,     ElectricRange: row.`Electric Range`,     BaseMSRP: row.`Base MSRP`,     LegislativeDistrict: row.`Legislative District`,     DOLVehicleID: row.`DOL Vehicle ID`,     VehicleLocation: row.`Vehicle Location`,     ElectricUtility: row.`Electric Utility`,     CensusTract2020: row.`2020 Census Tract`})")
        # Main Menu Loop
        while True:
            graphchoice = input("Choose what visualization you want to make: Piechart, HeatMap, BarPlot" )
            if (graphchoice == "Piechart"):
                var = input("Enter a column name to create a pie chart")

                query = f"MATCH (c:VehicleRegistration) WITH c.{var} AS {var} RETURN {var} ORDER BY {var}"
                plotdata.plotdata.createpieChart(plotdata, query, connection, var)
            if (graphchoice == "HeatMap"):
                var = input("Enter two column names to create a scattor plot. Enter first one:")
                var2 = input("Second One:")
                query = f"MATCH (c:VehicleRegistration) WITH c.{var} AS {var}, c.{var2} AS {var2} RETURN {var},{var2}"
                plotdata.plotdata.createheatmap(plotdata, query, connection, var, var2)
            if (graphchoice == "BarPlot"):
                var = input("Enter a column name to create a bar chart")

                query = f"MATCH (c:VehicleRegistration) WITH c.{var} AS {var} RETURN {var} ORDER BY {var}"
                plotdata.plotdata.createbarPlot(plotdata, query, connection, var)
            else:
                print("Invalid choice. Please enter 'Piechart', 'HeatMap', or 'BarChartr'.")

    if __name__ == '__main__':
        main()
