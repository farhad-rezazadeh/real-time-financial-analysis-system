import chartComponent from "./chart.mjs"

async function menuComponent() {
     await getData()
}

const appendComponent = (data) => {

    const sideBarList = document.getElementsByClassName("sidebar-list")[0]
    data.forEach(item => {
       let listItem = document.createElement("li");
    
       listItem.innerHTML =  `
       <li class="sidebar-list-item">
        <a class="menu-item">
        <span>${item?.stock_symbol}</span>
        <span id="${item?.status}">${item?.status}</span>
        </a>
       </li>
      `
       sideBarList.appendChild(listItem)
       listItem.addEventListener("click", () => filterFunction(item.stock_symbol));
   });
    

}

const filterFunction = async (type) => {
            
          switch (type){
                case "AAPL" : await chartComponent(`data/stock-data/?stock_symbol=${type}`); break
                case "TSL" : await chartComponent(`data/stock-data/?stock_symbol=${type}`); break
                case "GOOGL" : await chartComponent(`data/stock-data/?stock_symbol=${type}`); break
                case "AMZN" : await chartComponent(`data/stock-data/?stock_symbol=${type}`); break
                case "MSFT" : await chartComponent(`data/stock-data/?stock_symbol=${type}`); break
                default : await chartComponent('data/stock-data/?format=json')
          }
          
}

document.getElementById('no_filter').addEventListener('click' , async () => {
    await filterFunction("no_filter")
})

const getData = async () => {
    const response = await fetch(`http://127.0.0.1:8000/data/stock-list/?format=json`)
    const data = await response.json()
    appendComponent(data)
}

export default menuComponent;