document.addEventListener('DOMContentLoaded', () => {
    fetch('http://your-backend-api/recommendations')
        .then(response => response.json())
        .then(data => displayBooks(data))
        .catch(error => console.error('Error fetching recommendations:', error));
});

function displayBooks(books) {
    const booksContainer = document.getElementById('books');
    books.forEach(book => {
        const bookElement = document.createElement('div');
        bookElement.classList.add('book');
        
        const imgElement = document.createElement('img');
        imgElement.src = book.image_url;
        imgElement.alt = book.title;
        
        const titleElement = document.createElement('h3');
        titleElement.textContent = book.title;
        
        const authorElement = document.createElement('p');
        authorElement.textContent = `Author: ${book.author}`;
        
        const yearElement = document.createElement('p');
        yearElement.textContent = `Year: ${book.year}`;
        
        const publisherElement = document.createElement('p');
        publisherElement.textContent = `Publisher: ${book.publisher}`;
        
        bookElement.appendChild(imgElement);
        bookElement.appendChild(titleElement);
        bookElement.appendChild(authorElement);
        bookElement.appendChild(yearElement);
        bookElement.appendChild(publisherElement);
        
        booksContainer.appendChild(bookElement);
    });
}
