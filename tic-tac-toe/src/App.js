import React, { useState } from 'react';
import './App.css'; // Optional: If you want to add custom styling

function App() {
  const [turn, setTurn] = useState('X');
  const [board, setBoard] = useState(Array(9).fill(''));
  const [winner, setWinner] = useState(null);

  const checkWinner = (newBoard) => {
    const winPatterns = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ];

    for (let pattern of winPatterns) {
      const [a, b, c] = pattern;
      if (newBoard[a] && newBoard[a] === newBoard[b] && newBoard[a] === newBoard[c]) {
        return newBoard[a];
      }
    }
    return null;
  };

  const handleClick = (index) => {
    if (board[index] || winner) return;

    const newBoard = [...board];
    newBoard[index] = turn;
    setBoard(newBoard);

    const newWinner = checkWinner(newBoard);
    if (newWinner) {
      setWinner(newWinner);
    } else {
      setTurn(turn === 'X' ? 'O' : 'X');
    }
  };

  const resetGame = () => {
    setBoard(Array(9).fill(''));
    setTurn('X');
    setWinner(null);
  };

  return (
    <div className="App">
      <h1>Tic Tac Toe</h1>
      <div className="board">
        {board.map((value, index) => (
          <button key={index} onClick={() => handleClick(index)}>
            {value}
          </button>
        ))}
      </div>
      <h2>{winner ? `Player ${winner} Wins!` : `Turn: Player ${turn}`}</h2>
      <button onClick={resetGame}>Play Again</button>
    </div>
  );
}

export default App;