export default function getResponseFromAPI() {
const myPromise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
        return success;
    } else {
        return false;
    }
});
return myPromise;
}