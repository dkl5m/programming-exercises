/*
function tests(){
    return new Promise(function(resolve,reject)){
        const error = false;
        if(error){
            reject('Error...');
        }else{
            resolve("Promise was succesfully solved!");
        }
    }
}

tests().then(function(res){
    alert(res);
}).catch(function(err)){
    alert(err);
}
*/ //Promise

function tests(){
    return new Promise(function(resolve,reject)){
        setTimeout(function(){
            const error = false;
            if(error){
                reject('Error...');
            }else{
                resolve("Promise was succesfully solved!");
            }
        },2000)
    }
}

async function tests2(){
    await tests2().then(function(res){
        alert(res);
    });
    alert('hello!');
} 

tests2();

//use of await in asyncronows functions(just execute hello when the promise is resolved)