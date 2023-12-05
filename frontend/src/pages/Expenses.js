import React, { useState, useEffect } from 'react'
import axios from "axios";
import PageTitle from '../components/Typography/PageTitle'
import {
  Table,
  TableHeader,
  TableCell,
  TableBody,
  TableRow,
  TableFooter,
  TableContainer,
  Badge,
  Avatar,
  Button,
  Pagination,
  Label,
} from '@windmill/react-ui'
import { EditIcon, TrashIcon, MailIcon } from '../icons'

function Expenses() {
  const [page, setPage] = useState(1)
  const [data, setData] = useState([])
  const [totalResults, setTotalResults] = useState(0)

  const resultsPerPage = 10

  function onPageChange(p) {
    setPage(p)
  }

  function fetchExpenses(page) {
    axios
      .get(`/api/finance/expenses?page=${page}`)
      .then((res) => {
        setData(res.data.results)
        setTotalResults(res.data.count)
      })
      .catch((err) => console.log(err));
  }

  useEffect(() => {
    fetchExpenses(page)
  }, [page, totalResults])

  return (
    <>
      <PageTitle>Expenses</PageTitle>
      <Label>
        <div className="relative text-gray-500 focus-within:text-purple-600 dark:focus-within:text-purple-400">
          <input
            className="block w-full pl-10 mt-1 text-sm text-black dark:text-gray-300 dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:focus:shadow-outline-gray form-input"
            placeholder="Search"
          />
          <div className="absolute inset-y-0 flex items-center ml-3 pointer-events-none">
            <MailIcon className="w-5 h-5" aria-hidden="true" />
          </div>
        </div>
      </Label>

      {
        totalResults <= 0 ?
        <></> :
        <TableContainer className="mb-8">
        <Table>
          <TableHeader>
            <tr>
              <TableCell>Title</TableCell>
              <TableCell>Amount</TableCell>
              <TableCell>Status</TableCell>
              <TableCell>Date</TableCell>
              <TableCell>Actions</TableCell>
            </tr>
          </TableHeader>
          <TableBody>
            {data.map((expense, i) => (
              <TableRow key={i}>
                <TableCell>
                  <div className="flex items-center text-sm">
                    {/* <Avatar className="hidden mr-3 md:block" src={expense.avatar} alt="expense avatar" /> */}
                    <div>
                      <p className="font-semibold">{expense.title}</p>
                      <p className="text-xs text-gray-600 dark:text-gray-400">{expense.title}</p>
                    </div>
                  </div>
                </TableCell>
                <TableCell>
                  <span className="text-sm">$ {expense.value}</span>
                </TableCell>
                <TableCell>
                  <Badge type={expense.checked}>{expense.checked}</Badge>
                </TableCell>
                <TableCell>
                  <span className="text-sm">{new Date(expense.created_at).toLocaleDateString()}</span>
                </TableCell>
                <TableCell>
                  <div className="flex items-center space-x-4">
                    <Button layout="link" size="icon" aria-label="Edit">
                      <EditIcon className="w-5 h-5" aria-hidden="true" />
                    </Button>
                    <Button layout="link" size="icon" aria-label="Delete">
                      <TrashIcon className="w-5 h-5" aria-hidden="true" />
                    </Button>
                  </div>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
        <TableFooter>
          <Pagination
              totalResults={totalResults}
              resultsPerPage={resultsPerPage}
              onChange={onPageChange}
            />
        </TableFooter>
      </TableContainer>
      }
    </>
  )
}



export default Expenses
