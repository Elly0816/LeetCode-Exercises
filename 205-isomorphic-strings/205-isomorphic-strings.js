/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const mapper = {};
    if (s.length !== t.length){
        return false;
    };
    
    for (let i=0; i<s.length; i++){
        if (!mapper.hasOwnProperty(s[i]) && !Object.values(mapper).includes(t[i])){
            mapper[s[i]] = t[i];
        };
    };
    
    for (let i=0; i<s.length; i++){
        if (mapper[s[i]] !== t[i]){
            return false;
        };
    };
    return true;
};