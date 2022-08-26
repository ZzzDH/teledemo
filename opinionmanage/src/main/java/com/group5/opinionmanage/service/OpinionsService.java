package com.group5.opinionmanage.service;

import com.group5.opinionmanage.entity.Opinions;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

/**
 * @author 10569
 * @version 1.0
 * @description     提供的服务接口
 * @Date 2022/8/24 15:17
 */

public interface OpinionsService {
    Opinions findByOid(Integer oid);
    Page<Opinions> findByContext(Pageable pageable,String context);
    Page<Opinions> findAll(Pageable pageable);
    Long count();

    Page<Opinions> findByType(Pageable pageable,String id);
    Page<Opinions> findByKeyWord(Pageable pageable,String keyword);
}


