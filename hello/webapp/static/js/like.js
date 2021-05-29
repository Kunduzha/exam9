// let url = 'article:like_article'


async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    if (response.ok) {  // нормальный ответ
        return await response.json();
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}



async function likeArticle(event) {
    event.preventDefault();
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        let id = a.dataset.article_counter
        let counter = document.getElementById(id)
        counter.innerText = response
        console.log(response);
        a.innerHTML = '<i class="bi bi-heart-fill"></i>'
        a.onclick = unlikeArticle
        a.setAttribute('href', url.replace('like_article', "unlike_article"))
    }
    catch (error){
        console.log(error);
    }
}

async function unlikeArticle(event){
    event.preventDefault();
    let a = event.currentTarget;
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        let id = a.dataset.article_counter
        let counter = document.getElementById(id)
        counter.innerText = response
        console.log(response);
        a.innerHTML = '<i class="bi bi-heart"></i>'
        a.onclick = likeArticle
        a.setAttribute('href', url.replace('unlike_article', "like_article"))
    }
    catch (error){
        console.log(error);
    }

}

async function likeComment(event) {
    event.preventDefault();
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        let id = a.dataset.comment_counter
        console.log(id)
        let counter = document.getElementById(id)
        counter.innerText = response
        console.log(response);
        a.innerHTML = '<i class="bi bi-heart-fill"></i>'
        a.onclick = unlikeComment
        a.setAttribute('href', url.replace('like_comment', "unlike_comment"))
    }
    catch (error){
        console.log(error);
    }
}

async function unlikeComment(event){
    event.preventDefault();
    let a = event.currentTarget;
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        let id = a.dataset.comment_counter
        let counter = document.getElementById(id)
        counter.innerText = response
        console.log(response);
        a.innerHTML = '<i class="bi bi-heart"></i>'
        a.onclick = likeComment
        a.setAttribute('href', url.replace('unlike_comment', "like_comment"))
    }
    catch (error){
        console.log(error);
    }

}