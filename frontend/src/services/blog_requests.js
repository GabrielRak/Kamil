import axios from 'axios';

export async function fetchPosts() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/blog/posts/');
    return response.data; 
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error; 
  }
}


export async function fetchPost(id) {
  try{
    const response = await axios.get('http://localhost:8000/blog/posts/' + id);
    return response.data;
  }catch (error) {
    console.error('Error fetching data:', error);
    throw error; 
  }
}