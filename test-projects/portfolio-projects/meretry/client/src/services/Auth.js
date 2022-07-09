import Client from './api'

export const SignInUser = async (data) => {
    try {
        const res = await Client.post('/auth/login', data)
        localStorage.setItem('token', res.data.token)
        console.log(res.data)
        return res.data.user
    } catch (err) {throw err}
}
  
export const RegisterUser = async (data) => {
    console.log("HEre")
    try {
        const res = await Client.post('/auth/register', data)
        console.log(res)
        return res.data
    } catch (err) {throw err}
}
  
export const CheckSession = async () => {
    try {
        const res = await Client.get('/auth/session')
        return res.data
    } catch (err) {throw err}
}