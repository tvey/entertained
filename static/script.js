const categorySelect = document.getElementById('categorySelect');
const genreSelect = document.getElementById('genreSelect');
const yearSelect = document.getElementById('yearSelect');
const searchForm = document.getElementById('search');
const showAllBtn = document.getElementById('show-all');
let genreElems = document.querySelectorAll('.genre');

loadEventListeners();

function loadEventListeners() {

  categorySelect.addEventListener('change', (event) => {
    let category = event.target.value;
    let param = `category=${category}`;
    fetchAPIData('f', param);
    genreSelect.value = '-1';
    yearSelect.value = '-1';
    searchForm.reset();
  });

  genreSelect.addEventListener('change', (event) => {
    let genre = event.target.value;
    let param = `genre=${genre}`;
    fetchAPIData('f', param);
    categorySelect.value = '-1';
    yearSelect.value = '-1';
    searchForm.reset();
  });

  yearSelect.addEventListener('change', (event) => {
    let yearSort = event.target.value;
    let param = `year=${yearSort}`;
    fetchAPIData('f', param);
    categorySelect.value = '-1';
    genreSelect.value = '-1';
    searchForm.reset();
  });

  searchForm.addEventListener('keyup', (event) => {
    const userInput = event.target.value;
    if (userInput) {
      let param = `q=${userInput}`;
      fetchAPIData('f', param);
    } else {
      fetchAPIData('everything');
    }
    categorySelect.value = '-1';
    genreSelect.value = '-1';
    yearSelect.value = '-1';
    event.preventDefault();
  });

  genreElems.forEach(genreElem => {
    genreElem.addEventListener('click', () => {
      let genreName = genreElem.innerText;
      let param = `genreName=${genreName}`;
      fetchAPIData('f', param);
      categorySelect.value = '-1';
      yearSelect.value = '-1';
      searchForm.reset();
    })
  })

  showAllBtn.addEventListener('click', (event) => {
    fetchAPIData('everything');
    event.preventDefault();
  });

}

async function fetchAPIData(route, param = null) {
  let url = `/${route}`;

  if (param) {
    url = `${url}?${param}`
  }

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      fillTable(data);
    })
    .catch(err => console.log(err));
}


function createNothing() {
  let nothing = document.createElement('h4');
  nothing.appendChild(document.createTextNode('Nothing found ¯\\_(ツ)_/¯'));
  nothing.className = 'text-center mt-2';
  nothing.setAttribute('id', 'nothing');
  return nothing;
}

function fillTable(data) {
  const tbody = document.querySelector('#entertained tbody');
  const nothing = document.getElementById('nothing');

  if (data.length) {
    let rows = '';
    data.forEach(item => {
      let genres = '';
      item.genres.forEach(genre => {
        genres += `<span class="badge bg-primary">${genre}</span>\n`

      });

      let row = `
        <tr>
          <td>${item.category}</td>
          <td>${item.title}</td>
          <td>${item.creators}</td>
          <td>${item.year}</td>
          <td>${genres}</td>
        </tr>
      `;
      rows = rows + row;
    });
    tbody.innerHTML = rows;
    if (nothing) {
      nothing.remove();
    }
  } else {
    if (document.getElementById('nothing') === null) {
      document.querySelector('main').appendChild(createNothing());
    }
    tbody.innerHTML = '';
  }
}