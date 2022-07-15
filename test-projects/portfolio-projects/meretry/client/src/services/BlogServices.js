import { toBeInTheDOM } from "@testing-library/jest-dom/dist/matchers";
import Client from "./api";


export const GetPosts = async () => {
    try{
        const res = await Client.get('posts/')
        // console.log(res)
        return res.data
    }catch(err){throw err}
}

export const GetPostById = async (id) => {
    try{
        const res = await Client.get(`posts/${id}`)
        // console.log(res)
        return res.data
    }catch(err){throw err}
}

export const CreatePost = async (newPost, id) => {
    console.log(newPost, "BEfore TRY")
    try {
        const data = {
            title: newPost.title,
            text: newPost.text,
            name: newPost.name,
            user_id: id
        }
        console.log(data, "Before axios")
        await Client.post(`posts/`, data)
        .then((res) => console.log(res, "successfully projected"))
        .catch((err) => console.log(err))
    } catch (err) {
        throw err
    } 
}

export const RemovePost = async (id) => {
    try{
        await Client.delete(`posts/delete/${id}`)
        .then((res) => console.log(res, "Successfully deleted post"))
        .catch((err) => console.log(err))
    } catch (err) {
        throw err
    }
}