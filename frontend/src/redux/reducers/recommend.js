import { RECOMMENDATION_SUCCESS , RECOMMENDATION_LOADING, RECOMMENDATION_FAILURE} from '../actions/recommend/types'

export default function reducer(state = {}, action) {
    switch(action.type) {
        case RECOMMENDATION_SUCCESS: 
            return {
                ...action.payload,
                loading:false
            }
        case RECOMMENDATION_LOADING:
            return { 
                ...state,
                loading:true
            }    
        case RECOMMENDATION_FAILURE:
            return { 
                ...state,
                error: action.error.data,
                loading:false
            }
        default:
            return state
    }
}
