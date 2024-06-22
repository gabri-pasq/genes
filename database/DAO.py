from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCromosmi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct (Chromosome)
                    from genes g 
                    where Chromosome != 0"""
        cursor.execute(query)
        for row in cursor:
            result.append(row['Chromosome'])
        cursor.close()
        conn.close()
        return sorted(result)


    @staticmethod
    def getArchi(partenza,arrivo):
        conn = DBConnect.get_connection()
        result = None
        cursor = conn.cursor(dictionary=True)
        query = """select sum(i.Expression_Corr)as peso
                    from interactions i  
                    where i.GeneID1 in (select GeneID from genes g where g.Chromosome=%s)
		            and i.GeneID2 in (select GeneID from genes g where g.Chromosome=%s)"""
        cursor.execute(query,(partenza,arrivo,))
        for row in cursor:
            result=(row['peso'])
        cursor.close()
        conn.close()
        return result

