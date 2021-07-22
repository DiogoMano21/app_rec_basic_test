import axios from 'axios'

import { RECOMMENDATION_SUCCESS, RECOMMENDATION_FAILURE, RECOMMENDATION_LOADING} from './types'

// GET /top-searched?interval=<interval>&topRange=<topRange>
export function recommend(app_id) {
    const params =  { app_id:app_id}
    const headers = { "Content-Type": "Access-Control-Allow-Origin" }
    axios.defaults.headers.get['Content-Type'] ='application/x-www-form-urlencoded';
    return (dispatch) => {
        dispatch(recommendLoading())
        axios.get('http://192.168.1.85:5000/recommend',{params: params},{headers: headers})
        .then(response => {
            //console.log(response)
            dispatch(recommendSuccess(response))})
        .catch(error => dispatch(recommendFailure(error)))
    }
}
export const recommendLoading = () => ({
    type: RECOMMENDATION_LOADING,
    loading: true
})
export const recommendSuccess = (response) => ({
    type: RECOMMENDATION_SUCCESS,
    payload: response.data
})

export const recommendFailure = (error) => ({
    type: RECOMMENDATION_FAILURE,
    error: { error }
})
