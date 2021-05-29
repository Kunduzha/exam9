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



async function choiceAlbom(event) {
    event.preventDefault();
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        a.innerHTML = '<i class="bi bi-bookmark-fill">'
        a.onclick = unchoiceAlbom
        a.setAttribute('href', url.replace('choice_albom', "unchoice_albom"))
    }
    catch (error){
        console.log(error);
    }
}

async function unchoiceAlbom(event){
    event.preventDefault();
    let a = event.currentTarget;
    let url = a.getAttribute('href');
    try {
        let response = await makeRequest(url)
        console.log(response);
        a.innerHTML = '<i class="bi bi-bookmark"></i>'
        a.onclick = choiceAlbom
        a.setAttribute('href', url.replace('unchoice_albom', "choice_albom"))
    }
    catch (error){
        console.log(error);
    }

}

async function choiceGallery(event) {
    event.preventDefault();
    let a = event.currentTarget
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url)
        console.log(response);
        a.innerHTML = '<i class="bi bi-bookmark-fill">'
        a.onclick = unchoiceGallery
        a.setAttribute('href', url.replace('choice_gallery', "unchoice_gallery"))
    }
    catch (error){
        console.log(error);
    }
}

async function unchoiceGallery(event){
    event.preventDefault();
    let a = event.currentTarget;
    let url = a.getAttribute('href')
    try {
        let response = await makeRequest(url);

        a.innerHTML = '<i class="bi bi-bookmark"></i>'
        a.onclick = likeComment
        a.setAttribute('href', url.replace('unchoice_gallery', "choice_gallery"))
    }
    catch (error){
        console.log(error);
    }

}