#!/usr/bin/python 

import sys
import csv

directoryPath="./"

class Table:
    _rowNum = 0
    _columnNum = 0

    _rowHeadder=[]
    _columnHeadder=[]
    _table=[]

    # getter of table size 
    def getRowNum(self):
        return _rowNum

    def getColumnNum(self):
        return _columnNum
  
    # accesor of table headder
    def getRowHeadder(self):
        return self._rowHeadder
 
    def setRowHeadder(self, headder):
        self._rowHeadder = headder
    
    def getColumnHeadder(self):
        return self._columnHeadder
 
    def setColumnHeadder(self, headder):
        self._columnHeadder = headder

    # accesor of table data
    def getRow(self, key):
        return self._table[key]
 
    def setRow(self, key, row):
        rowIdx = self._rowHeadder.index(key)
        self._table.insert(rowIdx, row)
    
    def getColumn(self, key):
        columnIdx = self._columnHeadder.index(key)
        column = []
        for row in _table:
            column.append(row[columnIdx])
        return column
 
    def setColumn(self, key, column):
        columnIdx = self._columnHeadder.index(key)
        for i in len(table):
            table[i].insert(columnIdx, column[i])

def main():
    mct = Table()

    mct.setColumnHeadder(["a", "b", "c", "d", "e"])
    mct.setRowHeadder(["cp1", "cp2", "cp3"])
    mct.setRow("cp1", [1, 2, 3, 4, 5])

    print(mct._table)

if "__main__" == __name__:
    main()
