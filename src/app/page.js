import data from '@/data/data.json'
console.log(data)

const gridSquares = [
  "Config",
  ...data.scenes
]

export default function Home() {
  
  return (
    <main className="flex ">
      {
        gridSquares.map((item, index) => {
          return(
            <div key={index}>
              {/* {item} */}asdf
            </div>
          )
        })
      }
    </main>
  )
}



