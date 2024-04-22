import dbconnection



class main:
    ''''Main app class for weather update app'''

    def main():
       d = dbconnection.dbconnection("config.yaml")
       connection = d.get_neo_connection()
       connection.verify_connectivity()
       connection.execute_query("LOAD CSV WITH HEADERS FROM 'C:\Users\evant\PycharmProjects\FinalProject\Electric_Vehicle_Population_Data.csv' AS line CREATE (:registration { VIN: line.`VIN`), County: line.`County`, Country: line.Country, ItemType: line.`Item Type`, SalesChannel: line.`Sales Channel`, OrderPriority: line.`Order Priority`, OrderDate: line.`Order Date`, ShipDate: line.`Ship Date`, UnitSold: toInteger(line.UnitsSold), UnitPrice: toFloat(line.UnitPrice), UnitCost: toFloat(line.UnitCost), TotalRevenue: toFloat(line.TotalRevenue), TotalCost: toFloat(line.TotalCost), TotalProfit: toFloat(line.TotalProfit)})")


    if __name__ == '__main__':
        main()
